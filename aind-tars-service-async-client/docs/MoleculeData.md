# MoleculeData

MoleculeData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**molecule_type** | [**MoleculeType**](MoleculeType.md) |  | [optional] 
**state** | [**AnyOf**](AnyOf.md) |  | [optional] 
**aliases** | [**List[Alias]**](Alias.md) |  | [optional] [default to []]
**citations** | **List[object]** |  | [optional] [default to []]
**rr_id** | [**AnyOf**](AnyOf.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**addgene_id** | [**AnyOf**](AnyOf.md) |  | [optional] 
**mgi_id** | [**AnyOf**](AnyOf.md) |  | [optional] 
**notes** | [**AnyOf**](AnyOf.md) |  | [optional] 
**sequence** | **str** |  | [optional] 
**genes** | **List[object]** |  | [optional] [default to []]
**loci** | **List[object]** |  | [optional] [default to []]
**species** | [**List[Species]**](Species.md) |  | [optional] [default to []]
**organizations** | **List[object]** |  | [optional] [default to []]
**shipments** | **List[object]** |  | [optional] [default to []]
**material_transfer_agreements** | **List[object]** |  | [optional] [default to []]
**gen_bank_files** | **List[str]** |  | [optional] [default to []]
**map_files** | **List[str]** |  | [optional] [default to []]
**fasta_files** | **List[str]** |  | [optional] [default to []]
**parents** | **List[object]** |  | [optional] [default to []]
**children** | **List[object]** |  | [optional] [default to []]
**patents** | **List[object]** |  | [optional] [default to []]
**creators** | **List[object]** |  | [optional] [default to []]
**principal_investigator** | [**AnyOf**](AnyOf.md) |  | [optional] 
**targeted_cell_populations** | [**List[TargetedCellPopulation]**](TargetedCellPopulation.md) |  | [optional] [default to []]
**validated_cell_populations** | **List[object]** |  | [optional] [default to []]
**targeted_rois** | [**List[TargetedRoi]**](TargetedRoi.md) |  | [optional] [default to []]
**validated_rois** | **List[object]** |  | [optional] [default to []]
**genome_coordinates** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from aind_tars_service_async_client.models.molecule_data import MoleculeData

# TODO update the JSON string below
json = "{}"
# create an instance of MoleculeData from a JSON string
molecule_data_instance = MoleculeData.from_json(json)
# print the JSON string representation of the object
print(MoleculeData.to_json())

# convert the object into a dict
molecule_data_dict = molecule_data_instance.to_dict()
# create an instance of MoleculeData from a dict
molecule_data_from_dict = MoleculeData.from_dict(molecule_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


