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

    <div
      style={{
        padding: "40px",
        fontFamily: "Arial"
      }}
    >

      <h1>
        AI Red Team Platform
      </h1>

      <br />

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

          <div>

            <h2>
              Assessment Result
            </h2>

            <p>
              Overall Score:
              {" "}
              {result.overall_score}
            </p>

            <p>
              Overall Rating:
              {" "}
              {result.overall_rating}
            </p>

            <pre>
              {
                JSON.stringify(
                  result,
                  null,
                  2
                )
              }
            </pre>

          </div>
        )
      }

    </div>
  );
}

export default App;