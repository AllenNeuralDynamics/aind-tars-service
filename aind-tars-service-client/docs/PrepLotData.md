# PrepLotData

PrepLotData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**lot** | **str** |  | [optional] 
**date_prepped** | **datetime** |  | [optional] 
**viral_prep** | [**ViralPrep**](ViralPrep.md) |  | [optional] 
**titers** | [**List[Titers]**](Titers.md) |  | [optional] [default to []]

## Example

```python
from aind_tars_service_client.models.prep_lot_data import PrepLotData

# TODO update the JSON string below
json = "{}"
# create an instance of PrepLotData from a JSON string
prep_lot_data_instance = PrepLotData.from_json(json)
# print the JSON string representation of the object
print(PrepLotData.to_json())

# convert the object into a dict
prep_lot_data_dict = prep_lot_data_instance.to_dict()
# create an instance of PrepLotData from a dict
prep_lot_data_from_dict = PrepLotData.from_dict(prep_lot_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


