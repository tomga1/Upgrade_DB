    CREATE TABLE tmpArticulos (
        ItemCode NVARCHAR(50),
        ItemName NVARCHAR(200),
        tMon NVARCHAR(3) DEFAULT 'PSO',
        RubroCod NVARCHAR(50),
        SubRubroCod NVARCHAR(50),
        MarcaCod NVARCHAR(50),
        IvaRate FLOAT,
        Habilitado CHAR(1),
        CreateDate DATE,
        UpdateDate DATE
    );