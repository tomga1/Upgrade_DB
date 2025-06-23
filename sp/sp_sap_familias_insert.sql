CREATE PROCEDURE sp_sap_familias_insert(
	@xdescripcion varchar(60)
)
AS
BEGIN
	DECLARE @vExiste int;
	DECLARE @vProximoID int;
	
	SET @vExiste = (SELECT 
						COUNT(*)
					FROM 
						familias 
					WHERE 
						familias.descripcio = @xdescripcion);
	IF @vExiste = 0 
	BEGIN
		SET @vProximoID = (SELECT MAX(familias.idFamilia) + 1 FROM familias);
		INSERT INTO familias (
			idFamilia, descripcio, usuAlta, fecAlta, idHostAlta)
		VALUES (
			@vProximoID, @xdescripcion, 'SAP', CURRENT_TIMESTAMP, 'SAP # UPGRADE');
	END;
		
END
GO