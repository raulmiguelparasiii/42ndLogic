from .agent import Candidate, Inquiry, OneLogicSolver, StaticGenerator, TableReality


def main() -> None:
    # Four candidate structured explanations. The actual environment corresponds to h3,
    # but the solver is not given that identity directly.
    candidates = [
        Candidate("h1", "fault=A", {"sensor": "low", "load": "stable", "reset": "fails"}),
        Candidate("h2", "fault=B", {"sensor": "high", "load": "stable", "reset": "works"}),
        Candidate("h3", "fault=C", {"sensor": "high", "load": "rising", "reset": "fails"}),
        Candidate("h4", "fault=D", {"sensor": "low", "load": "rising", "reset": "works"}),
    ]
    inquiries = [
        Inquiry("sensor", cost=1),
        Inquiry("load", cost=1),
        Inquiry("reset", cost=2),
    ]
    reality = TableReality({"sensor": "high", "load": "rising", "reset": "fails"})

    solver = OneLogicSolver(StaticGenerator(candidates), reality, inquiries)
    result = solver.solve("Which fault explains the observed system?")

    print("status:", result.status)
    print("answer:", result.answer)
    print("live:", result.live_candidate_ids)
    print("observations:")
    for obs in result.trace.observations:
        print(f"  {obs.inquiry_id} -> {obs.outcome}")


if __name__ == "__main__":
    main()
