# ViralPrepType

ViralPrepType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from aind_tars_service_client.models.viral_prep_type import ViralPrepType

# TODO update the JSON string below
json = "{}"
# create an instance of ViralPrepType from a JSON string
viral_prep_type_instance = ViralPrepType.from_json(json)
# print the JSON string representation of the object
print(ViralPrepType.to_json())

# convert the object into a dict
viral_prep_type_dict = viral_prep_type_instance.to_dict()
# create an instance of ViralPrepType from a dict
viral_prep_type_from_dict = ViralPrepType.from_dict(viral_prep_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


