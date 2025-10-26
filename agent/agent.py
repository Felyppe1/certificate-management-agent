from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext
import requests
from typing import Optional
from .env import BACKEND_URL, ADK_MODEL

def get_certificate_emissions(tool_context: ToolContext):
    """Fetch all the user's certificate emission details."""
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions"
        resp = requests.get(url, headers=headers, timeout=120)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching certificate emissions: {str(e)}"}


def create_certificate_emission(tool_context: ToolContext, name: str):
    """Create a new certificate emission with the given name.
    
    Args:
        name: The name of the certificate emission (1-100 characters)
    """
    print(f"[create_certificate_emission] name={name}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions"
        body = {"name": name}
        resp = requests.post(url, json=body, headers=headers, timeout=120)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error creating certificate emission: {str(e)}"}


def add_template_by_url(tool_context: ToolContext, certificate_emission_id: str, file_url: str):
    """Add/replace a template to a certificate emission using a file URL.
    
    Args:
        certificate_emission_id: The ID of the certificate emission
        file_url: The URL of the template file to add
    """
    print(f"[add_template_by_url] certificate_emission_id={certificate_emission_id}, file_url={file_url}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions/{certificate_emission_id}/templates/url"
        body = {"fileUrl": file_url}
        resp = requests.put(url, json=body, headers=headers, timeout=120)
        resp.raise_for_status()
        return {"success": True, "message": "Template added successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error adding template: {str(e)}"}


def add_data_source_by_url(tool_context: ToolContext, certificate_emission_id: str, file_url: str):
    """Add/replace a data source to a certificate emission using a file URL.
    
    Args:
        certificate_emission_id: The ID of the certificate emission
        file_url: The URL of the data source file to add
    """
    print(f"[add_data_source_by_url] certificate_emission_id={certificate_emission_id}, file_url={file_url}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions/{certificate_emission_id}/data-sources/url"
        body = {"fileUrl": file_url}
        resp = requests.put(url, json=body, headers=headers, timeout=120)
        resp.raise_for_status()
        return {"success": True, "message": "Data source added successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error adding data source: {str(e)}"}


def delete_template(tool_context: ToolContext, certificate_emission_id: str):
    """Delete the template from a certificate emission.
    
    Args:
        certificate_emission_id: The ID of the certificate emission
    """
    print(f"[delete_template] certificate_emission_id={certificate_emission_id}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions/{certificate_emission_id}/templates"
        resp = requests.delete(url, headers=headers, timeout=120)
        resp.raise_for_status()
        return {"success": True, "message": "Template deleted successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error deleting template: {str(e)}"}


def delete_data_source(tool_context: ToolContext, certificate_emission_id: str):
    """Delete the data source from a certificate emission.
    
    Args:
        certificate_emission_id: The ID of the certificate emission
    """
    print(f"[delete_data_source] certificate_emission_id={certificate_emission_id}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions/{certificate_emission_id}/data-sources"
        resp = requests.delete(url, headers=headers, timeout=120)
        resp.raise_for_status()
        return {"success": True, "message": "Data source deleted successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error deleting data source: {str(e)}"}


def refresh_template(tool_context: ToolContext, certificate_emission_id: str):
    """Refresh/update the template data from its original source.
    
    Args:
        certificate_emission_id: The ID of the certificate emission
    """
    print(f"[refresh_template] certificate_emission_id={certificate_emission_id}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions/{certificate_emission_id}/templates"
        resp = requests.patch(url, headers=headers, timeout=120)
        resp.raise_for_status()
        return {"success": True, "message": "Template refreshed successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error refreshing template: {str(e)}"}


def refresh_data_source(tool_context: ToolContext, certificate_emission_id: str):
    """Refresh/update the data source from its original source.
    
    Args:
        certificate_emission_id: The ID of the certificate emission
    """
    print(f"[refresh_data_source] certificate_emission_id={certificate_emission_id}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions/{certificate_emission_id}/data-sources"
        resp = requests.patch(url, headers=headers, timeout=120)
        resp.raise_for_status()
        return {"success": True, "message": "Data source refreshed successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error refreshing data source: {str(e)}"}


def update_certificate_emission(tool_context: ToolContext, certificate_emission_id: str, name: Optional[str] = None, variable_column_mapping: Optional[dict] = None):
    """Update a certificate emission's name and/or variable-column mapping (the user will likely write the mapping in a conversational way).
    
    Args:
        certificate_emission_id: The ID of the certificate emission
        name: New name for the certificate emission (optional, 1-100 characters)
        variable_column_mapping: Dictionary mapping template variables to data source columns (optional)
    """
    print(f"[update_certificate_emission] certificate_emission_id={certificate_emission_id}, name={name}, variable_column_mapping={variable_column_mapping}")
    
    session_token = tool_context.state.get("session_token")
    
    if not session_token:
        return {"error": "User session token not found"}
    
    if not name and not variable_column_mapping:
        return {"error": "At least one of 'name' or 'variable_column_mapping' must be provided"}
    
    try:
        headers = {"Authorization": f"Bearer {session_token}"}
        url = f"{BACKEND_URL}/api/certificate-emissions/{certificate_emission_id}"
        body = {}
        if name is not None:
            body["name"] = name
        if variable_column_mapping is not None:
            body["variableColumnMapping"] = variable_column_mapping
        
        resp = requests.put(url, json=body, headers=headers, timeout=120)
        resp.raise_for_status()
        return {"success": True, "message": "Certificate emission updated successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error updating certificate emission: {str(e)}"}


PROMPT = '''
You are an intelligent agent that helps users to manage or answer questions about their certificate emissions.
Most of the tools to perform actions on certificate emissions will require the certificate emission ID, which you can obtain by first listing the user's certificate emissions.
The user will likely ask you to perform actions based on the names of the certificate emissions, so you will need to map those names to their corresponding IDs from the list you retrieve.
Pay attention when the user asks for mapping template variables to data source columns.
- he can mean to keep the current mapping and just change specific ones
- he can mean to to override everything
- he may not say the name of the variables or columns exactly how they are named in the system (in this case, if it is obvious what he means, do it; otherwise, ask for confirmation before doing it)
'''

root_agent = Agent(
    model=ADK_MODEL,
    name='root_agent',
    description='A helpful agent for the certificate emission system.',
    instruction=PROMPT,
    tools=[
        get_certificate_emissions,
        create_certificate_emission,
        add_template_by_url,
        add_data_source_by_url,
        delete_template,
        delete_data_source,
        refresh_template,
        refresh_data_source,
        update_certificate_emission,
    ],
)