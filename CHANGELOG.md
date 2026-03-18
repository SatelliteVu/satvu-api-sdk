## [0.5.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.5.0...v0.5.1) (2026-03-12)

## [0.5.1.20260318.1607] - 2026-03-18

### feat(reseller): update GET /companies, POST /search/companies

#### GET /companies
* added the required property 'companies/items/country_code' to the response with the '200' status


#### POST /search/companies
* added the required property 'companies/items/country_code' to the response with the '200' status


## [0.5.1.20260317.1156] - 2026-03-17

### feat(cos): update 7 endpoints

#### GET /{contract_id}/
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### POST /{contract_id}/
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '201' status
* removed the optional property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '201' status
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '201'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '201'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '201'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '201'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '201'
* the 'coordinates' response's property default value '[]' was removed for the status '201'
* the 'coordinates' response's property default value '[]' was removed for the status '201'
* the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '201'
* the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '201'
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '201' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '201' status


#### POST /{contract_id}/price
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status


#### POST /{contract_id}/search/
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### GET /{contract_id}/{order_id}
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### PATCH /{contract_id}/{order_id}
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### GET /{contract_id}/{order_id}/{item_id}/download
* for the 'path' request parameter 'item_id', the maxLength was set to '256'

#### Description Updates
* 167 description(s) modified


## [0.5.1.20260317.1057] - 2026-03-17

### feat(otm): update API descriptions

#### Description Updates
* 4 description(s) modified



### Bug Fixes

* **builder:** resolve relative $ref paths in OpenAPI specs

# [0.5.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.4.0...v0.5.0) (2026-01-20)

## [0.5.0.20260127.1235] - 2026-01-27

### feat(wallet): update API descriptions

#### Description Updates
* 4 description(s) modified


## [0.5.0.20260127.1115] - 2026-01-27

### feat(cos): update 5 endpoints

#### GET /{contract_id}/
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### POST /{contract_id}/
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'


#### POST /{contract_id}/search/
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### GET /{contract_id}/{order_id}
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### PATCH /{contract_id}/{order_id}
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'

#### Description Updates
* 1 description(s) modified



### Features

* **builder:** add hypothesis example caching for faster tests

# [0.4.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.3.1...v0.4.0) (2026-01-15)


### Features

* **builder:** add conditional test generation via SATVU_GENERATE_TESTS
* **build:** exclude tests and builder from wheel distribution

## [0.3.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.3.0...v0.3.1) (2026-01-14)


### Bug Fixes

* **auth:** handle malformed JWTs in expiration check
* **auth:** make MemoryCache instance-level to prevent token leakage
* **misc:** export OpenAPI spec cache from Dagger container
* **release:** set git identity before creating annotated tag

# [0.3.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.2.0...v0.3.0) (2026-01-07)

## [0.3.0.20260113.1752] - 2026-01-13

### feat(reseller): update API descriptions

#### Description Updates
* 1 description(s) modified


## [0.3.0.20260113.1724] - 2026-01-13

### feat(id): update API descriptions

#### Description Updates
* 4 description(s) modified


## [0.3.0.20260112.1536] - 2026-01-12

### feat(policy): update API descriptions

#### Description Updates
* 6 description(s) modified


## [0.3.0.20260112.1243] - 2026-01-12

### feat(otm): update API descriptions

#### Description Updates
* 2 description(s) modified



### Bug Fixes

* handle pook mock responses in stdlib adapter streaming
* **misc:** include scope in changelog entries
* **release:** anchor version grep to start of line


### Features

* add Jinja2 templates for streaming download tests
* integrate streaming test generation into build

# [0.2.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.1...v0.2.0) (2025-12-19)

### Features

- **core:** rename package and module to satvu
- **release:** implement timestamp versioning for API-triggered releases

## [0.1.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.0...v0.1.1) (2025-12-19)

### Bug Fixes

- **core:** add docstring for SatVuSDK.__init__

# [0.1.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.0.0...v0.1.0) (2025-12-19)

### Features

- **core:** add docstring for the SatVuSDK class
