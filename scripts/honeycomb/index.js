import { HoneycombWebSDK, WebVitalsInstrumentation } from '@honeycombio/opentelemetry-web';
import { getWebAutoInstrumentations } from '@opentelemetry/auto-instrumentations-web';

window.initHoneycomb = function (apiKey) {
  if (!apiKey) return;

  const sdk = new HoneycombWebSDK({
    apiKey: apiKey,
    serviceName: 'rougarou',
    instrumentations: [getWebAutoInstrumentations(), new WebVitalsInstrumentation()],
  });
  sdk.start();
};
