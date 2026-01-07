# local-warp-agent

**Sovereign Local AI Agent System with Warp-like UI**

Run multi-agent orchestration locally on your machine with zero cloud dependencies. Built for developers who need deterministic, auditable AI agents.

## Features

✅ **Local-First Architecture** - Zero external API calls, complete sovereignty  
✅ **Multi-Agent Orchestration** - Run 3-4 concurrent agents with intelligent coordination  
✅ **Ollama Integration** - Uses local LLMs (Mistral, Llama, Qwen) for inference  
✅ **MCP Tool Protocol** - Extensible tool system (file ops, CLI, git, code search)  
✅ **Terminal Dashboard** - Real-time monitoring of agent status and tool execution  
✅ **Complete Audit Logging** - Every agent decision and tool call logged  
✅ **Permission-Based Security** - Allowlist/denylist controls for CLI and file access  

## Quick Start

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.ai) installed locally
- 8GB+ RAM recommended
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/AXI0MH1VE/local-warp-agent.git
cd local-warp-agent

# Install dependencies
pip install -r requirements.txt

# Start Ollama (in a separate terminal)
ollama serve

# Pull a local model
ollama pull mistral

# Launch the agent system
python agent_launcher.py
```

### Basic Usage

```bash
# Run with default settings (interactive mode)
python agent_launcher.py

# Execute a specific task
python agent_launcher.py --task "code-builder:Create a REST API for user management"

# Use a specific model
python agent_launcher.py --model llama3

# Run with custom agent count
python agent_launcher.py --agents 2
```

## Architecture

```
local-warp-agent/
├── agent_launcher.py          # Main entry point
├── requirements.txt            # Python dependencies
├── config/
│   ├── agents.yaml            # Agent definitions & prompts
│   └── tools.yaml             # Tool configurations & permissions
├── agents/
│   ├── orchestrator.py        # Multi-agent coordinator
│   ├── executor.py            # Tool execution engine
│   ├── logger.py              # Audit logging system
│   └── tools/
│       ├── file_system.py     # File operations (read/write/search)
│       ├── cli_executor.py    # Terminal command execution
│       ├── code_search.py     # Codebase indexing & search
│       └── git_integration.py # Git operations
├── ui/
│   └── dashboard.py           # Terminal UI dashboard
└── logs/                       # Audit trail storage
```

## Configuration

### Agent Configuration (`config/agents.yaml`)

Define custom agents with specific roles, models, and tool access:

```yaml
agents:
  - id: code-builder
    name: "Code Builder"
    model: "mistral"
    system_prompt: "You are an expert software engineer..."
    tools:
      - file_system
      - cli_executor
      - code_search
    max_iterations: 10
```

### Tool Configuration (`config/tools.yaml`)

Set permissions and constraints for each tool:

```yaml
tools:
  cli_executor:
    allowlist:
      - "ls"
      - "cat"
      - "grep"
    denylist:
      - "rm -rf"
      - "sudo"
    timeout: 30
```

## Available Agents

### 1. **Code Builder**
- Creates new code files and modules
- Implements features based on requirements
- Uses: file_system, cli_executor, code_search

### 2. **Documentation Writer**  
- Generates technical documentation
- Creates README files and API docs
- Uses: file_system, code_search

### 3. **Refactor Specialist**
- Improves code quality and structure
- Applies design patterns
- Uses: file_system, code_search, git_integration

### 4. **Test Engineer**
- Writes unit and integration tests
- Runs test suites
- Uses: file_system, cli_executor, code_search

## Available Tools (MCP)

### File System (`file_system.py`)
- `read_file(path)` - Read file contents
- `write_file(path, content)` - Write to file
- `list_directory(path)` - List directory contents
- `search_files(pattern)` - Search files by pattern

### CLI Executor (`cli_executor.py`)
- `execute_command(cmd)` - Run shell commands
- Sandboxed execution with allowlist/denylist
- Timeout protection

### Code Search (`code_search.py`)
- `search_code(query)` - Semantic code search
- `find_definition(symbol)` - Find symbol definitions
- `get_context(file, line)` - Get code context

### Git Integration (`git_integration.py`)
- `git_status()` - Check repository status
- `git_diff()` - View changes
- `git_commit(message)` - Create commits

## Terminal Dashboard

The dashboard provides real-time monitoring:

```
╔══════════════════════════════════════════════════════════╗
║  LOCAL WARP AGENT SYSTEM                                 ║
╠══════════════════════════════════════════════════════════╣
║  Active Agents: 3/4                                      ║
║  Tasks Completed: 12                                     ║
║  Uptime: 00:45:23                                        ║
╠══════════════════════════════════════════════════════════╣
║  Agent: code-builder          [RUNNING]                  ║
║    → Executing: write_file                               ║
║    → Status: Writing API routes...                       ║
║                                                          ║
║  Agent: docs-writer           [IDLE]                     ║
║    → Last: Generated README.md                           ║
║                                                          ║
║  Agent: refactor              [THINKING]                 ║
║    → Status: Analyzing code structure...                 ║
╚══════════════════════════════════════════════════════════╝
```

## Security & Permissions

### Built-in Safeguards

1. **CLI Command Filtering** - Only approved commands can execute
2. **File Access Control** - Restrict file operations to specific directories
3. **Timeout Protection** - Long-running operations auto-terminate
4. **Audit Logging** - Full trail of all agent actions
5. **No External API Calls** - Everything runs locally

### Permission Model

Define granular permissions in `config/tools.yaml`:

```yaml
tools:
  file_system:
    allowed_paths:
      - "./src"
      - "./tests"
    denied_paths:
      - "./.env"
      - "./secrets"
  
  cli_executor:
    allowlist:
      - "pytest"
      - "npm test"
    denylist:
      - "rm"
      - "dd"
```

## Audit Logs

All agent activities are logged to `logs/` with:

- Timestamp
- Agent ID
- Tool calls with parameters
- Results and errors
- Decision reasoning

Example log:

```json
{
  "timestamp": "2026-01-06T23:15:42Z",
  "agent_id": "code-builder",
  "tool": "file_system.write_file",
  "params": {"path": "src/api.py", "content": "..."},
  "result": "success",
  "reasoning": "Creating new API endpoint"
}
```

## Advanced Usage

### Custom Agent Creation

```python
from agents.orchestrator import AgentOrchestrator
from agents.tools import FileSystemTool, CLIExecutorTool

# Define custom agent
orchestrator = AgentOrchestrator(
    model="mistral",
    tools=[FileSystemTool(), CLIExecutorTool()]
)

# Run custom task
orchestr ator.run("Build a Python CLI tool")
```

### Integration with Existing Projects

Add to your existing codebase:

```python
import sys
sys.path.append('./local-warp-agent')

from agents.orchestrator import AgentOrchestrator

# Use agents programmatically
agent = AgentOrchestrator.from_config('config/agents.yaml')
result = agent.execute_task("Refactor this module")
```

## Performance

**Typical Performance on 16GB RAM Lenovo Laptop:**

- Startup time: ~5 seconds
- Agent spawn time: ~2 seconds
- Tool execution: 50-500ms
- Memory per agent: ~800MB
- CPU usage: 20-40% during active reasoning

**Recommended Models:**

- **Mistral 7B** - Best balance (4GB VRAM)
- **Llama 3 8B** - Fast inference (5GB VRAM)
- **Qwen 2.5 7B** - Code-optimized (4GB VRAM)

## Troubleshooting

### Ollama Connection Failed
```bash
# Ensure Ollama is running
ollama serve

# Test connection
curl http://localhost:11434/api/tags
```

### Agent Timeout
Increase timeout in `config/agents.yaml`:
```yaml
agents:
  - id: my-agent
    timeout: 120  # seconds
```

### Permission Denied
Check tool permissions in `config/tools.yaml` and ensure paths are accessible.

## Roadmap

- [ ] Web-based dashboard (alternative to terminal)
- [ ] Agent-to-agent communication protocols
- [ ] Built-in code review agent
- [ ] Integration with VS Code extension
- [ ] Docker containerization
- [ ] Multi-machine agent distribution

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-tool`)
3. Commit your changes (`git commit -m 'Add amazing tool'`)
4. Push to the branch (`git push origin feature/amazing-tool`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Credits

Built by the [AXIOM HIVE](https://github.com/AXI0MH1VE) team.

Inspired by:
- Warp AI's agentic development environment
- Model Context Protocol (MCP)
- Local-first software principles

## Support

- **Issues**: [GitHub Issues](https://github.com/AXI0MH1VE/local-warp-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AXI0MH1VE/local-warp-agent/discussions)
- **Documentation**: [Wiki](https://github.com/AXI0MH1VE/local-warp-agent/wiki)

---

**Built with sovereignty in mind. Your code, your agents, your machine.**
