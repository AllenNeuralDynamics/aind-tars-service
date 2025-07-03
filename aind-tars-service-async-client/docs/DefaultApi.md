# aind_tars_service_async_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_molecules**](DefaultApi.md#get_molecules) | **GET** /molecules/{name} | Get Molecules
[**get_viral_prep_lots**](DefaultApi.md#get_viral_prep_lots) | **GET** /viral_prep_lots/{lot} | Get Viral Prep Lots
[**get_viruses**](DefaultApi.md#get_viruses) | **GET** /viruses/{name} | Get Viruses


# **get_molecules**
> List[MoleculeData] get_molecules(name, page_size=page_size, limit=limit)

Get Molecules

## TARS Endpoint to molecule data.

### Example


```python
import aind_tars_service_async_client
from aind_tars_service_async_client.models.molecule_data import MoleculeData
from aind_tars_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_tars_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_tars_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_tars_service_async_client.DefaultApi(api_client)
    name = 'AiP20611' # str | 
    page_size = 1 # int | Number of items to return in a single page. (optional) (default to 1)
    limit = 1 # int | Limit number of items returned. Set to 0 to return all. (optional) (default to 1)

    try:
        # Get Molecules
        api_response = await api_instance.get_molecules(name, page_size=page_size, limit=limit)
        print("The response of DefaultApi->get_molecules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_molecules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **page_size** | **int**| Number of items to return in a single page. | [optional] [default to 1]
 **limit** | **int**| Limit number of items returned. Set to 0 to return all. | [optional] [default to 1]

### Return type

[**List[MoleculeData]**](MoleculeData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viral_prep_lots**
> List[PrepLotData] get_viral_prep_lots(lot, page_size=page_size, limit=limit)

Get Viral Prep Lots

## TARS Endpoint to retrieve viral prep lot data.
Retrieves viral prep lot information from TARS for a prep_lot_id.

### Example


```python
import aind_tars_service_async_client
from aind_tars_service_async_client.models.prep_lot_data import PrepLotData
from aind_tars_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_tars_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_tars_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_tars_service_async_client.DefaultApi(api_client)
    lot = 'VT3214g' # str | 
    page_size = 1 # int | Number of items to return in a single page. (optional) (default to 1)
    limit = 1 # int | Limit number of items returned. Set to 0 to return all. (optional) (default to 1)

    try:
        # Get Viral Prep Lots
        api_response = await api_instance.get_viral_prep_lots(lot, page_size=page_size, limit=limit)
        print("The response of DefaultApi->get_viral_prep_lots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_viral_prep_lots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lot** | **str**|  | 
 **page_size** | **int**| Number of items to return in a single page. | [optional] [default to 1]
 **limit** | **int**| Limit number of items returned. Set to 0 to return all. | [optional] [default to 1]

### Return type

[**List[PrepLotData]**](PrepLotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viruses**
> List[VirusData] get_viruses(name, page_size=page_size, limit=limit)

Get Viruses

## TARS Endpoint to virus data.

### Example


```python
import aind_tars_service_async_client
from aind_tars_service_async_client.models.virus_data import VirusData
from aind_tars_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_tars_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with aind_tars_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_tars_service_async_client.DefaultApi(api_client)
    name = 'VIR300002_PHPeB' # str | 
    page_size = 1 # int | Number of items to return in a single page. (optional) (default to 1)
    limit = 1 # int | Limit number of items returned. Set to 0 to return all. (optional) (default to 1)

    try:
        # Get Viruses
        api_response = await api_instance.get_viruses(name, page_size=page_size, limit=limit)
        print("The response of DefaultApi->get_viruses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_viruses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **page_size** | **int**| Number of items to return in a single page. | [optional] [default to 1]
 **limit** | **int**| Limit number of items returned. Set to 0 to return all. | [optional] [default to 1]

### Return type

[**List[VirusData]**](VirusData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

