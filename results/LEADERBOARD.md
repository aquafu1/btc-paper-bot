# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 761 windows, 20996 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 395 | 33.7 | 34.9 | $-301.45 | -7.6% | $698.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2146 | 51.4 | 50.6 | $-535.96 | -2.5% | $464.04 | -1.2 | done | can't tell from luck |
| value_ev10 | 960 | 37.9 | 39.1 | $-627.58 | -6.5% | $372.42 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1776 | 49.9 | 49.6 | $-692.07 | -3.9% | $307.93 | -1.6 | done | can't tell from luck |
| trend_filter | 1237 | 49.8 | 50.9 | $-819.03 | -6.6% | $180.97 | -2.4 | done | losing for real |
| value_ev5 | 1449 | 40.2 | 41.1 | $-846.64 | -5.8% | $153.36 | -1.9 | done | can't tell from luck |
| coinflip | 3037 | 50.4 | 50.3 | $-1136.85 | -3.7% | $-136.85 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1776 | 50.1 | 51.2 | $-1222.01 | -6.9% | $-222.01 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2146 | 48.6 | 50.2 | $-1554.97 | -7.2% | $-554.97 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3037 | 50.8 | 51.7 | $-1656.48 | -5.5% | $-656.48 | -3.1 | done | losing for real |
| always_up | 3037 | 47.0 | 49.6 | $-2879.28 | -9.5% | $-1879.28 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4761 | 48.2 | 49.1 | $-2914.60 |
| ETH | 5233 | 48.0 | 48.6 | $-3488.80 |
| SOL | 5471 | 48.0 | 48.6 | $-3330.53 |
| XRP | 5531 | 48.6 | 48.5 | $-2538.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
