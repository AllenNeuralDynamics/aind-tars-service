# Species

Species

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ror_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from aind_tars_service_client.models.species import Species

# TODO update the JSON string below
json = "{}"
# create an instance of Species from a JSON string
species_instance = Species.from_json(json)
# print the JSON string representation of the object
print(Species.to_json())

# convert the object into a dict
species_dict = species_instance.to_dict()
# create an instance of Species from a dict
species_from_dict = Species.from_dict(species_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


