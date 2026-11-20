import os

from fastmcp import FastMCP

from tools import (get_credit_hours, marks_to_grade_points,
                   calculate_cgpa, required_gpa_for_target)

mcp = FastMCP("cgpa")

# mcp.tool(fn) turns a plain function into an MCP tool.
# Docstring + type hints = the description the model reads.
mcp.tool(get_credit_hours)
mcp.tool(marks_to_grade_points)
mcp.tool(calculate_cgpa)
mcp.tool(required_gpa_for_target)

if __name__ == "__main__":
    # Local: http://127.0.0.1:8000/mcp   Hosting (Render etc.) sets PORT and needs 0.0.0.0
    mcp.run(transport="http",
            host=os.environ.get("HOST", "127.0.0.1"),
            port=int(os.environ.get("PORT", 8000)))
