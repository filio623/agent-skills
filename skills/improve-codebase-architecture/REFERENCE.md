# Reference

## Dependency Categories

When assessing a candidate for deepening, classify its dependencies.

### 1. In-Process

Pure computation, in-memory state, no I/O.

Always deepenable: merge the modules and test directly.

### 2. Local-Substitutable

Dependencies that have local test stand-ins, such as PGLite for Postgres or an in-memory filesystem.

Deepenable if the test substitute exists. The deepened module is tested with the local stand-in running in the test suite.

### 3. Remote But Owned

Your own services across a network boundary: microservices, internal APIs, queues, or owned workers.

Define a port at the module boundary. The deep module owns the logic and the transport is injected. Tests use an in-memory adapter. Production uses the real HTTP, gRPC, queue, or worker adapter.

Recommendation shape:

```text
Define a shared interface, implement a production adapter and an in-memory test adapter, so the logic can be tested as one deep module even though it is deployed across a network boundary.
```

### 4. True External

Third-party services you do not control, such as Stripe, Twilio, or external APIs.

Mock at the boundary. The deepened module takes the external dependency as an injected port, and tests provide a mock implementation.

## Testing Strategy

The core principle: replace, do not layer.

- Delete old unit tests on shallow modules once boundary tests cover the same behavior.
- Write new tests at the deepened module's public interface.
- Assert observable outcomes through the public interface, not internal state.
- Make tests describe behavior so they survive internal refactors.

## RFC Template

```markdown
## Problem

Describe the architectural friction:

- Which modules are shallow and tightly coupled.
- What integration risk exists in the seams between them.
- Why this makes the codebase harder to navigate and maintain.

## Proposed Interface

Describe the chosen interface design:

- Interface signature, types, methods, and parameters.
- Usage example showing how callers use it.
- Complexity it hides internally.

## Dependency Strategy

State which category applies and how dependencies are handled:

- In-process: merged directly.
- Local-substitutable: tested with a specific stand-in.
- Ports and adapters: port definition, production adapter, test adapter.
- Mock: mock boundary for external services.

## Testing Strategy

- New boundary tests to write.
- Old tests to delete.
- Test environment needs, such as local stand-ins or adapters.

## Implementation Recommendations

Durable architectural guidance that is not coupled to current file paths:

- What the module should own.
- What it should hide.
- What it should expose.
- How callers should migrate to the new interface.
```
