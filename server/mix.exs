defmodule PlanningAsAService.MixProject do
  use Mix.Project

  def project do
    [
      app: :planning_as_a_service,
      version: "26.8.27",
      elixir: "~> 1.18",
      start_permanent: Mix.env() == :prod,
      deps: deps(),
      aliases: aliases()
    ]
  end

  def application do
    [
      extra_applications: [:logger, :crypto],
      mod: {PlanningAsAService.Application, []}
    ]
  end

  defp deps do
    [
      {:ash, "~> 3.32"},
      {:ash_postgres, "~> 2.9"},
      {:ash_r2rml,
       git: "https://github.com/seanchatmangpt/ash_r2rml.git",
       ref: "067954ad406fd637fd47646bdb10c4580809c79d"},
      {:oban, "~> 2.23"},
      {:ecto_sql, "~> 3.13"},
      {:postgrex, ">= 0.0.0"},
      {:bandit, "~> 1.8"},
      {:plug, "~> 1.19"},
      {:jason, "~> 1.4"},
      {:b3, "~> 0.2"}
    ]
  end

  defp aliases do
    [
      verify: ["format --check-formatted", "compile --warnings-as-errors", "test"]
    ]
  end
end
