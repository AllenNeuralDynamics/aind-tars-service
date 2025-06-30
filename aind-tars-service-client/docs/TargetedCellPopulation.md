# TargetedCellPopulation

TargetedCellPopulation

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
from aind_tars_service_client.models.targeted_cell_population import TargetedCellPopulation

# TODO update the JSON string below
json = "{}"
# create an instance of TargetedCellPopulation from a JSON string
targeted_cell_population_instance = TargetedCellPopulation.from_json(json)
# print the JSON string representation of the object
print(TargetedCellPopulation.to_json())

# convert the object into a dict
targeted_cell_population_dict = targeted_cell_population_instance.to_dict()
# create an instance of TargetedCellPopulation from a dict
targeted_cell_population_from_dict = TargetedCellPopulation.from_dict(targeted_cell_population_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


