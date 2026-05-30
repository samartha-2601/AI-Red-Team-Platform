import { useState } from "react";
import api from "./services/api";

function App() {

  const [provider, setProvider] =
    useState("openai");

  const [target, setTarget] =
    useState("banking");

  const [result, setResult] =
    useState<any>(null);

  const [loading, setLoading] =
    useState(false);

  const runAssessment = async () => {

    setLoading(true);

    setResult(null);

    try {

      const response = await api.post(
        `/assess/${provider}/${target}`
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

      alert("Assessment failed");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="container">

      <h1 className="title">
        AI Red Team Platform
      </h1>

      <br />

      <div className="form-section">

        <label>
          Provider:
        </label>

        <br />

        <select
          value={provider}
          onChange={(e) =>
            setProvider(e.target.value)
          }
        >

          <option value="openai">
            OpenAI
          </option>

          <option value="ollama">
            Ollama
          </option>

        </select>

        <br />
        <br />

        <label>
          Target:
        </label>

        <br />

        <select
          value={target}
          onChange={(e) =>
            setTarget(e.target.value)
          }
        >

          <option value="banking">
            Banking
          </option>

          <option value="hr">
            HR
          </option>

          <option value="customer-support">
            Customer Support
          </option>

        </select>

        <br />
        <br />

        <button
          onClick={runAssessment}
          disabled={loading}
        >

          {
            loading
              ? "Running Assessment..."
              : "Run Assessment"
          }

        </button>
      </div>

      <br />
      <br />

      {
        loading && (

          <div>

            <h3>
              Running security assessment...
            </h3>

            <p>
              Executing prompt injection,
              jailbreak and role confusion
              attacks against the model.
            </p>

          </div>
        )
      }

      {
        result && (

          <>

            <div className="cards">

              <div className="card">

                <h3>
                  Overall Score
                </h3>

                <div className="card-value">
                  {result.overall_score}
                </div>

              </div>

              <div className="card">

                <h3>
                  Risk Rating
                </h3>

                <div
                  className={`card-value ${result.overall_rating.toLowerCase()}`}
                >
                  {result.overall_rating}
                </div>

              </div>

            </div>

            <div className="category-table">

              <h2>
                Attack Categories
              </h2>

              {

                Object.entries(
                  result.categories
                ).map(
                  ([name, category]: any) => {

                    const score =
                      (
                        category.successful_attacks /
                        category.total_attacks
                      ) * 100;

                    return (

                      <div
                        key={name}
                        className="category-row"
                      >

                        <span>
                          {name}
                        </span>

                        <span>
                          {score.toFixed(0)}%
                        </span>

                      </div>
                    );
                  }
                )
              }

            </div>

          </>
        )
      }

    </div>
  );
}

export default App;