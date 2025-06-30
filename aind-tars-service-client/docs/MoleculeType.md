# MoleculeType

MoleculeType

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
from aind_tars_service_client.models.molecule_type import MoleculeType

# TODO update the JSON string below
json = "{}"
# create an instance of MoleculeType from a JSON string
molecule_type_instance = MoleculeType.from_json(json)
# print the JSON string representation of the object
print(MoleculeType.to_json())

# convert the object into a dict
molecule_type_dict = molecule_type_instance.to_dict()
# create an instance of MoleculeType from a dict
molecule_type_from_dict = MoleculeType.from_dict(molecule_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


