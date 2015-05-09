-- Whole table schema
CREATE TABLE test (
    Request_MerchantID INT,
    Request_MetaData_list INT,
    Request_MetaData_list_Key VARCHAR(10) CHARACTER SET utf8,
    Request_Payer_Identity_ID INT,
    Request_SkuItems_list INT,
    Request_SkuItems_list_ItemDescription VARCHAR(100) CHARACTER SET utf8,
    Request_SkuItems_list_ItemPrice NUMERIC(20, 2),
    Request_SkuItems_list_ItemQuantity INT,
    Request_SkuItems_list_SKU VARCHAR(50) CHARACTER SET utf8,
    Request_SkuItems_list_SKUItemID INT,
    Request_SkuItems_list_UTCDateTimeAdded varchar(),
    Request_UTCDateTimeCreated varchar()
);
INSERT INTO test VALUES (123456789,NULL,'Value',NULL,NULL,'Onion Rings',2.99,2,'sm_orings',1692,NOW(),NOW());
-- test Select * from test;

-- Schema for SkuItems

CREATE TABLE Skultems (
    SkuItems_list INT,
    SkuItems_list_ItemDescription VARCHAR(100) CHARACTER SET utf8,
    SkuItems_list_ItemPrice NUMERIC(20, 2),
    SkuItems_list_ItemQuantity INT,
    SkuItems_list_SKU VARCHAR(50) CHARACTER SET utf8,
    SkuItems_list_SKUItemID INT,
    SkuItems_list_UTCDateTimeAdded varchar(50)
);
INSERT INTO Skultems VALUES (NULL,'Onion Rings',2.99,2,'sm_orings',1692,NOW()); 

-- test Select * from Skultems;

-- Schema for Payer
CREATE TABLE Payer (
    Identity_ID INT
);
INSERT INTO Payer VALUES (1);

-- test Select * from Payer;

-- Schema for Merchant
CREATE TABLE Merchant (
    MerchantID INT
);
INSERT INTO Merchant VALUES (123456789);

-- test Select * from Merchant;

