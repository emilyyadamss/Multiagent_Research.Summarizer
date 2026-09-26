# Hands-On Lab: Building 2-Agent System
Completed by Emily Adams, Lab given by Agentic AI Mastery Course

Build a 2-Agent System
Agents
Research Agent

Summarizer Agent

Features
Task passing

Structured outputs

Basic orchestration

Lab Goal
Build a simple multi-agent system where:

A user asks a question

The Research Agent gathers findings

The output is passed to the Summarizer Agent

The Summarizer Agent creates a clean final summary

A lightweight orchestrator controls the flow

What You Will Learn
How agents can have separate roles

How one agent passes work to another

How to enforce structured outputs

How to implement a simple orchestration loop

How multi-agent systems differ from a single prompt

Recommended Stack
Python

OpenAI or Claude API

Optional: Pydantic for structured outputs

Optional: mock search function instead of real web/API search

System Architecture
Flow
User Query
→ Research Agent
→ structured research notes
→ Summarizer Agent
→ final answer

## Set Up Steps 

- Install a virtual environment
- Install the requirements.txt 
- Export the Claude API key into the virtual environment 
- Create the .gitignore and place .venv, __pycache__, and other directories 

