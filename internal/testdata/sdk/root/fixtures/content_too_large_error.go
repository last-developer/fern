// Generated by Fern. Do not edit.

package api

import (
	json "encoding/json"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/root/fixtures/core"
)

type ContentTooLargeError struct {
	*core.APIError
	Body *Error
}

func (c *ContentTooLargeError) UnmarshalJSON(data []byte) error {
	body := new(Error)
	if err := json.Unmarshal(data, &body); err != nil {
		return err
	}
	c.StatusCode = 413
	c.Body = body
	return nil
}

func (c *ContentTooLargeError) MarshalJSON() ([]byte, error) {
	return json.Marshal(c.Body)
}
