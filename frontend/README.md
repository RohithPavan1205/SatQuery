# SatQuery AI - Frontend Foundation

This is the initial Frontend/GIS foundation for Team 1 of the SatQuery AI project. This frontend is currently a structural foundation; actual functionalities (like model queries, GIS rendering, API calls) will be implemented incrementally.

## 1. Tech Stack
- **Framework:** React
- **Language:** TypeScript
- **Build Tool:** Vite

## 2. Component Naming Convention
- Use PascalCase for component folder names and `.tsx` files (e.g., `Upload`, `SpatialEvidence`).
- Each component should reside in its own folder under `src/components/`, typically with an `index.tsx` as the main entry point.

## 3. Folder/Module Organization
The frontend structure is organized as follows:
- `src/components/`: Contains UI components grouped by feature (e.g., Upload, Query, Viewer, GIS, Results, etc.).
- `src/pages/`: Contains full-page layouts that compose multiple components.
- `src/services/`: Contains API and external service integration logic.
- `src/types/`: Contains shared TypeScript interfaces and types.
- `src/hooks/`: Contains custom, reusable React hooks.
- `src/utils/`: Contains generic utility functions and helpers.

## 4. API/Service Calls
- All frontend/backend communication will be placed in `src/services/`.
- API integration will be implemented after the API contract is finalized with Team 2.

## 5. Shared TypeScript Types
- Global types, request/response interfaces, and shared data models are located in `src/types/`.
- These types will correspond to the API contract.

## 6. GIS / GeoTIFF — Pending Selection
- GeoTIFF and GIS functionality will eventually live in `src/components/GIS/` and related utilities.
- **Note:** Team 1 will evaluate **Leaflet + georaster** and **MapLibre** and make the final selection before implementing the browser GeoTIFF demo. 
- GeoTIFF rendering is currently **not implemented**.

## 7. Reusable Hooks and Utilities
- Shared React logic (e.g., state management hooks, effect wrappers) lives in `src/hooks/`.
- Helper functions (e.g., data formatters, calculation utilities) live in `src/utils/`.

## 8. Modularity Rules
- Components must be modular and focused on a single responsibility.
- Avoid placing heavy business logic directly inside components. Delegate to hooks and services.
- Keep dependencies minimal.

## 9. State Management
- Keep state management simple for the initial phase.
- Use React's built-in `useState`, `useReducer`, and `useContext`.
- Do not introduce Redux or other external state-management libraries unless genuinely necessary.

## 10. Development Status
- This frontend is a **foundation**.
- It does not contain fake functionality, mock datasets, or fake API responses.
- Features such as Before/After Comparison, Spatial Evidence, Confidence Display, and Execution Summary have structural placeholders and will be implemented incrementally as the backend and API contracts mature.
