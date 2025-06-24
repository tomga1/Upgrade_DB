CREATE OR ALTER PROCEDURE sp_sap_marcas_insert(
	@xdescripcion VARCHAR(60)
)
AS
BEGIN
	DECLARE @vExiste INT;
	DECLARE @vProximoID INT;

	SET @vExiste = (SELECT COUNT(*) FROM marcas WHERE descripcio = @xdescripcion);

	IF @vExiste = 0
	BEGIN
		SET @vProximoID = (SELECT ISNULL(MAX(idMarca), 0) + 1 FROM marcas);

		INSERT INTO marcas (
			idMarca, descripcio, usuAlta, fecAlta, idHostAlta
		)
		VALUES (
			@vProximoID, @xdescripcion, 'SAP', CURRENT_TIMESTAMP, 'SAP_SERVER'
		);
	END;
END
GO
