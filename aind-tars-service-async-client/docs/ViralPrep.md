# ViralPrep

ViralPrep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**rr_id** | **str** |  | [optional] 
**viral_prep_type** | [**ViralPrepType**](ViralPrepType.md) |  | [optional] 
**virus** | [**VirusData**](VirusData.md) |  | [optional] 
**citations** | **List[object]** |  | [optional] [default to []]
**shipments** | **List[object]** |  | [optional] [default to []]
**patents** | **List[object]** |  | [optional] [default to []]
**material_transfer_agreements** | **List[object]** |  | [optional] [default to []]
**qc_certification_files** | **List[object]** |  | [optional] [default to []]
**serotypes** | **List[object]** |  | [optional] [default to []]

## Example

```python
from aind_tars_service_async_client.models.viral_prep import ViralPrep

# TODO update the JSON string below
json = "{}"
# create an instance of ViralPrep from a JSON string
viral_prep_instance = ViralPrep.from_json(json)
# print the JSON string representation of the object
print(ViralPrep.to_json())

# convert the object into a dict
viral_prep_dict = viral_prep_instance.to_dict()
# create an instance of ViralPrep from a dict
viral_prep_from_dict = ViralPrep.from_dict(viral_prep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


