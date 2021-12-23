module.exports = {
    extends: ["@commitlint/config-conventional"],
    rules: {
        "header-max-length": [0, "always", 100],
        "body-max-length": [0, "always", 100],
        "footer-max-length": [0, "always", 100],
        "header-case": [0, "always", "sentence-case"],
        "body-case": [0, "always", "sentence-case"],
    }
}