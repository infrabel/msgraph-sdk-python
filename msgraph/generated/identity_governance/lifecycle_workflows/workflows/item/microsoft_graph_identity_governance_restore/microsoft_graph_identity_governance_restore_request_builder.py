from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.identity_governance.workflow import Workflow
    from ......models.o_data_errors.o_data_error import ODataError

class MicrosoftGraphIdentityGovernanceRestoreRequestBuilder():
    """
    Provides operations to call the restore method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MicrosoftGraphIdentityGovernanceRestoreRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/microsoft.graph.identityGovernance.restore"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def post(self,request_configuration: Optional[MicrosoftGraphIdentityGovernanceRestoreRequestBuilderPostRequestConfiguration] = None) -> Optional[Workflow]:
        """
        Restore a workflow that has been deleted. You can only restore a workflow that was deleted within the last 30 days before Azure AD automatically permanently deletes it.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workflow]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.identity_governance.workflow import Workflow

        return await self.request_adapter.send_async(request_info, Workflow, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[MicrosoftGraphIdentityGovernanceRestoreRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Restore a workflow that has been deleted. You can only restore a workflow that was deleted within the last 30 days before Azure AD automatically permanently deletes it.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    @dataclass
    class MicrosoftGraphIdentityGovernanceRestoreRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
