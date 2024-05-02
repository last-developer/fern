/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as environments from "../../../../environments";
import * as core from "../../../../core";
import * as SeedTrace from "../../../index";
import urlJoin from "url-join";

export declare namespace Problem {
    interface Options {
        environment?: core.Supplier<environments.SeedTraceEnvironment | string>;
        token?: core.Supplier<core.BearerToken | undefined>;
        xRandomHeader?: core.Supplier<string | undefined>;
    }

    interface RequestOptions {
        timeoutInSeconds?: number;
        maxRetries?: number;
    }
}

export class Problem {
    constructor(protected readonly _options: Problem.Options = {}) {}

    /**
     * Creates a problem
     *
     * @example
     *     await seedTrace.problem.createProblem({
     *         problemName: "string",
     *         problemDescription: {
     *             boards: [{
     *                     type: "html",
     *                     value: "string"
     *                 }]
     *         },
     *         files: {
     *             [SeedTrace.Language.Java]: {
     *                 solutionFile: {
     *                     filename: "string",
     *                     contents: "string"
     *                 },
     *                 readOnlyFiles: [{
     *                         filename: "string",
     *                         contents: "string"
     *                     }]
     *             }
     *         },
     *         inputParams: [{
     *                 variableType: {
     *                     type: "integerType"
     *                 },
     *                 name: "string"
     *             }],
     *         outputType: {
     *             type: "integerType"
     *         },
     *         testcases: [{
     *                 testCase: {
     *                     id: "string",
     *                     params: [{
     *                             type: "integerValue",
     *                             value: 1
     *                         }]
     *                 },
     *                 expectedResult: {
     *                     type: "integerValue",
     *                     value: 1
     *                 }
     *             }],
     *         methodName: "string"
     *     })
     */
    public async createProblem(
        request: SeedTrace.CreateProblemRequest,
        requestOptions?: Problem.RequestOptions
    ): Promise<core.APIResponse<SeedTrace.CreateProblemResponse, SeedTrace.problem.createProblem.Error>> {
        const _response = await core.fetcher({
            url: urlJoin(
                (await core.Supplier.get(this._options.environment)) ?? environments.SeedTraceEnvironment.Prod,
                "/problem-crud/create"
            ),
            method: "POST",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Random-Header":
                    (await core.Supplier.get(this._options.xRandomHeader)) != null
                        ? await core.Supplier.get(this._options.xRandomHeader)
                        : undefined,
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/trace",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            body: request,
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
        });
        if (_response.ok) {
            return {
                ok: true,
                body: _response.body as SeedTrace.CreateProblemResponse,
            };
        }

        return {
            ok: false,
            error: SeedTrace.problem.createProblem.Error._unknown(_response.error),
        };
    }

    /**
     * Updates a problem
     *
     * @example
     *     await seedTrace.problem.updateProblem("string", {
     *         problemName: "string",
     *         problemDescription: {
     *             boards: [{
     *                     type: "html",
     *                     value: "string"
     *                 }]
     *         },
     *         files: {
     *             [SeedTrace.Language.Java]: {
     *                 solutionFile: {
     *                     filename: "string",
     *                     contents: "string"
     *                 },
     *                 readOnlyFiles: [{
     *                         filename: "string",
     *                         contents: "string"
     *                     }]
     *             }
     *         },
     *         inputParams: [{
     *                 variableType: {
     *                     type: "integerType"
     *                 },
     *                 name: "string"
     *             }],
     *         outputType: {
     *             type: "integerType"
     *         },
     *         testcases: [{
     *                 testCase: {
     *                     id: "string",
     *                     params: [{
     *                             type: "integerValue",
     *                             value: 1
     *                         }]
     *                 },
     *                 expectedResult: {
     *                     type: "integerValue",
     *                     value: 1
     *                 }
     *             }],
     *         methodName: "string"
     *     })
     */
    public async updateProblem(
        problemId: SeedTrace.ProblemId,
        request: SeedTrace.CreateProblemRequest,
        requestOptions?: Problem.RequestOptions
    ): Promise<core.APIResponse<SeedTrace.UpdateProblemResponse, SeedTrace.problem.updateProblem.Error>> {
        const _response = await core.fetcher({
            url: urlJoin(
                (await core.Supplier.get(this._options.environment)) ?? environments.SeedTraceEnvironment.Prod,
                `/problem-crud/update/${encodeURIComponent(problemId)}`
            ),
            method: "POST",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Random-Header":
                    (await core.Supplier.get(this._options.xRandomHeader)) != null
                        ? await core.Supplier.get(this._options.xRandomHeader)
                        : undefined,
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/trace",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            body: request,
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
        });
        if (_response.ok) {
            return {
                ok: true,
                body: _response.body as SeedTrace.UpdateProblemResponse,
            };
        }

        return {
            ok: false,
            error: SeedTrace.problem.updateProblem.Error._unknown(_response.error),
        };
    }

    /**
     * Soft deletes a problem
     *
     * @example
     *     await seedTrace.problem.deleteProblem("string")
     */
    public async deleteProblem(
        problemId: SeedTrace.ProblemId,
        requestOptions?: Problem.RequestOptions
    ): Promise<core.APIResponse<void, SeedTrace.problem.deleteProblem.Error>> {
        const _response = await core.fetcher({
            url: urlJoin(
                (await core.Supplier.get(this._options.environment)) ?? environments.SeedTraceEnvironment.Prod,
                `/problem-crud/delete/${encodeURIComponent(problemId)}`
            ),
            method: "DELETE",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Random-Header":
                    (await core.Supplier.get(this._options.xRandomHeader)) != null
                        ? await core.Supplier.get(this._options.xRandomHeader)
                        : undefined,
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/trace",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
        });
        if (_response.ok) {
            return {
                ok: true,
                body: undefined,
            };
        }

        return {
            ok: false,
            error: SeedTrace.problem.deleteProblem.Error._unknown(_response.error),
        };
    }

    /**
     * Returns default starter files for problem
     *
     * @example
     *     await seedTrace.problem.getDefaultStarterFiles({
     *         inputParams: [{
     *                 variableType: {
     *                     type: "integerType"
     *                 },
     *                 name: "string"
     *             }],
     *         outputType: {
     *             type: "integerType"
     *         },
     *         methodName: "string"
     *     })
     */
    public async getDefaultStarterFiles(
        request: SeedTrace.GetDefaultStarterFilesRequest,
        requestOptions?: Problem.RequestOptions
    ): Promise<
        core.APIResponse<SeedTrace.GetDefaultStarterFilesResponse, SeedTrace.problem.getDefaultStarterFiles.Error>
    > {
        const _response = await core.fetcher({
            url: urlJoin(
                (await core.Supplier.get(this._options.environment)) ?? environments.SeedTraceEnvironment.Prod,
                "/problem-crud/default-starter-files"
            ),
            method: "POST",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Random-Header":
                    (await core.Supplier.get(this._options.xRandomHeader)) != null
                        ? await core.Supplier.get(this._options.xRandomHeader)
                        : undefined,
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/trace",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            body: request,
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
        });
        if (_response.ok) {
            return {
                ok: true,
                body: _response.body as SeedTrace.GetDefaultStarterFilesResponse,
            };
        }

        return {
            ok: false,
            error: SeedTrace.problem.getDefaultStarterFiles.Error._unknown(_response.error),
        };
    }

    protected async _getAuthorizationHeader(): Promise<string | undefined> {
        const bearer = await core.Supplier.get(this._options.token);
        if (bearer != null) {
            return `Bearer ${bearer}`;
        }

        return undefined;
    }
}
