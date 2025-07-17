CREATE OR ALTER PROCEDURE dbo.ProcesarArticuloSAP
    @ItemCode NVARCHAR(50),
    @ItemName NVARCHAR(200),
    @tMon NVARCHAR(3) = 'PSO',
    @RubroCod NVARCHAR(50),
    @SubRubroCod NVARCHAR(50),
    @MarcaCod NVARCHAR(50),
    @IvaRate FLOAT,
    @Habilitado CHAR(1),
    @CreateDate DATE,
    @UpdateDate DATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Me aseguro que la tabla esté vacía antes de procesar.
    TRUNCATE TABLE tmpArticulos;

    -- Insertar datos en tabla temporal
    INSERT INTO tmpArticulos (
        ItemCode, ItemName, tMon, RubroCod, SubRubroCod, MarcaCod,
        IvaRate, Habilitado, CreateDate, UpdateDate
    )
    VALUES (
        @ItemCode, @ItemName, @tMon, @RubroCod, @SubRubroCod, @MarcaCod,
        @IvaRate, @Habilitado, @CreateDate, @UpdateDate
    );

    -- Ahora hacer el procesamiento sobre la tabla temporal, por ejemplo:
    DECLARE @habilitadoBit BIT = CASE WHEN @Habilitado = 'S' THEN 1 ELSE 0 END;
    DECLARE @idProv INT = 1; -- fijo

    -- Procesar registros de la tabla temporal (en este caso, solo 1 fila)
    DECLARE @idArticulo INT = NULL;

    SELECT @idArticulo = idArticulo
    FROM dbo.Articulos
    WHERE codArt = (
        SELECT TOP 1 ItemCode COLLATE SQL_Latin1_General_CP1_CI_AS
        FROM tmpArticulos
    );


    IF @idArticulo IS NOT NULL
    BEGIN
        UPDATE dbo.Articulos
        SET 
            descripcio = (SELECT TOP 1 ItemName FROM tmpArticulos),
            idFamilia = TRY_CAST((SELECT TOP 1 RubroCod FROM tmpArticulos) AS INT),
            idSubFam = TRY_CAST((SELECT TOP 1 SubRubroCod FROM tmpArticulos) AS INT),
            idMarca = TRY_CAST((SELECT TOP 1 MarcaCod FROM tmpArticulos) AS INT),
            alicIVA = (SELECT TOP 1 IvaRate FROM tmpArticulos),
            habilitado = @habilitadoBit,
            idProv = @idProv,
            fecModi = (SELECT TOP 1 UpdateDate FROM tmpArticulos)
        WHERE idArticulo = @idArticulo;
    END
    ELSE
    BEGIN

        DECLARE @nextId INT = ISNULL((SELECT MAX(idArticulo) + 1 FROM dbo.Articulos), 1);

        INSERT INTO dbo.Articulos
        (
            idArticulo, codArt, descripcio, tMon, idFamilia, idSubFam, idMarca, alicIVA,
            habilitado, idProv, fecAlta, fecModi
        )
        SELECT
            @nextId, 
            ItemCode, ItemName, tMon, TRY_CAST(RubroCod AS INT), TRY_CAST(SubRubroCod AS INT), TRY_CAST(MarcaCod AS INT), IvaRate,
            @habilitadoBit, @idProv, CreateDate, UpdateDate
        FROM tmpArticulos;
    END
END
