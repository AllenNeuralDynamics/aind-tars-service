# Titers

Ttiers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**is_preferred** | **bool** |  | [optional] 
**thawed_count** | **int** |  | [optional] 
**result** | **int** |  | [optional] 
**titer_type** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from aind_tars_service_client.models.titers import Titers

# TODO update the JSON string below
json = "{}"
# create an instance of Titers from a JSON string
titers_instance = Titers.from_json(json)
# print the JSON string representation of the object
print(Titers.to_json())

# convert the object into a dict
titers_dict = titers_instance.to_dict()
# create an instance of Titers from a dict
titers_from_dict = Titers.from_dict(titers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


