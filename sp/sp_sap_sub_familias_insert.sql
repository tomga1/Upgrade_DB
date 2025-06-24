CREATE OR ALTER PROCEDURE sp_sap_subfamilias_insert(
	@xdescripcion VARCHAR(60)
)
AS
BEGIN
	DECLARE @vExiste INT;
	DECLARE @vProximoID INT;

	SET @vExiste = (SELECT COUNT(*) FROM subfam WHERE descripcio = @xdescripcion);

	IF @vExiste = 0
	BEGIN
		SET @vProximoID = (SELECT ISNULL(MAX(idSubFam), 0) + 1 FROM subfam);

		INSERT INTO subfam (
			idSubFam, descripcio, usuAlta, fecAlta, idHostAlta
		)
		VALUES (
			@vProximoID, @xdescripcion, 'SAP', CURRENT_TIMESTAMP, 'SAP # UPGRADE'
		);
	END;
END
GO
