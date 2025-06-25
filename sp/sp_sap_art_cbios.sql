CREATE OR ALTER PROCEDURE sp_sap_art_cbios(
    @xcodArt VARCHAR(60),
    @prNuevo FLOAT
)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @idArticulo INT;
    DECLARE @prAnt FLOAT;
    DECLARE @porVar FLOAT;

    SELECT @idArticulo = idArticulo
    FROM articulos
    WHERE codArt = @xcodArt AND habilitado = 1;

    IF @idArticulo IS NULL
    BEGIN
        RAISERROR('Artículo no encontrado con esa descripción', 16, 1);
        RETURN;
    END

    SELECT TOP 1 @prAnt = prNuevo
    FROM art_cbios
    WHERE idArticulo = @idArticulo
    ORDER BY fecha DESC;

    IF @prAnt IS NULL
        SET @prAnt = @prNuevo;


    IF @prAnt > 0
        set @porVar = ROUND (((@prNuevo - @prAnt) / @prAnt) * 100, 2);
    ELSE
        SET @porVar = 0;

    DECLARE @nuevoId INT = (SELECT ISNULL(MAX(idArtCbios), 0) + 1 FROM art_cbios);

    INSERT INTO art_cbios (idArtCbios, idArticulo, fecha, prAnt, prNuevo, porVar)
    VALUES (@nuevoId, @idArticulo, GETDATE(), @prAnt, @prNuevo, @porVar);
END; 
