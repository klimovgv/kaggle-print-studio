# Print Studio Agent

## Overview

Print Studio Agent is an AI-powered consultation system that streamlines the process of creating custom printed merchandise. The system uses multi-agent orchestration to collect client requirements, generate design assets, and prepare finalized briefs for merchandise production.

## Problem Statement

Printing merchandise requires collecting a formalized brief from clients, and generating multiple preview images is easy with latest genai models as nano banana. This project automates the entire workflow, from initial consultation through design generation to final brief preparation.

## Key Features

- **Consultant Agent**: Conducts a friendly, conversational interview with clients to gather merchandise design requirements including:
  - Project description and design style
  - Color palette and text preferences
  - Mood and target audience
  - Product selection (t-shirts, caps, pens)
  - Logo file validation or generation

- **Logo Generator Agent**: Creates custom logos based on client descriptions using generative AI

- **Finalizer Agent**: Prepares a polished, structured design brief for client presentation

## Architecture

The system uses a hierarchical multi-agent architecture:
- **Root Agent**: Orchestrates the consultation flow and manages sub-agents
- **Sub-agents**: Specialized agents for logo generation and brief finalization
- **Tools**: Logo file validation and registration

## Technology Stack

- Google Gemini 2.5 Flash models for natural language processing and image generation
- Google ADK (Agent Development Kit) for multi-agent orchestration
- Python-based implementation with retry logic and error handling

## Getting Started

1. Set up environment variables in `.env`
2. Initialize the agent system
3. Start a conversation with the root agent to begin the consultation process

The system will guide clients through a structured interview, collect all necessary information, and generate a comprehensive design brief ready for production.