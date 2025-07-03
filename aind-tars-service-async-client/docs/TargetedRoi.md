# TargetedRoi

TargetedRoi

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
from aind_tars_service_async_client.models.targeted_roi import TargetedRoi

# TODO update the JSON string below
json = "{}"
# create an instance of TargetedRoi from a JSON string
targeted_roi_instance = TargetedRoi.from_json(json)
# print the JSON string representation of the object
print(TargetedRoi.to_json())

# convert the object into a dict
targeted_roi_dict = targeted_roi_instance.to_dict()
# create an instance of TargetedRoi from a dict
targeted_roi_from_dict = TargetedRoi.from_dict(targeted_roi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


