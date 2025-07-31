# VirusData

Virus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**rr_id** | **str** |  | [optional] 
**aliases** | [**List[Alias]**](Alias.md) |  | [optional] [default to []]
**capsid** | **Dict[str, object]** |  | [optional] 
**citations** | **List[object]** |  | [optional] [default to []]
**molecules** | **List[object]** |  | [optional] [default to []]
**other_molecules** | **List[object]** |  | [optional] [default to []]
**patents** | **List[object]** |  | [optional] [default to []]

## Example

```python
from aind_tars_service_client.models.virus_data import VirusData

# TODO update the JSON string below
json = "{}"
# create an instance of VirusData from a JSON string
virus_data_instance = VirusData.from_json(json)
# print the JSON string representation of the object
print(VirusData.to_json())

# convert the object into a dict
virus_data_dict = virus_data_instance.to_dict()
# create an instance of VirusData from a dict
virus_data_from_dict = VirusData.from_dict(virus_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


