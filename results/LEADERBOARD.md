# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 893 windows, 24639 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 462 | 35.7 | 34.9 | $-81.30 | -1.8% | $918.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1131 | 38.2 | 39.1 | $-619.52 | -5.5% | $380.48 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2081 | 49.9 | 49.8 | $-956.48 | -4.6% | $43.52 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2515 | 50.5 | 50.4 | $-986.12 | -3.9% | $13.88 | -2.0 | done | can't tell from luck |
| trend_filter | 1451 | 50.0 | 51.0 | $-999.41 | -6.9% | $0.59 | -2.7 | done | losing for real |
| value_ev5 | 1711 | 39.9 | 41.0 | $-1024.05 | -6.0% | $-24.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2081 | 50.1 | 50.9 | $-1335.88 | -6.4% | $-335.88 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2515 | 49.5 | 50.4 | $-1406.48 | -5.6% | $-406.48 | -2.8 | done | losing for real |
| coinflip | 3564 | 50.3 | 50.3 | $-1505.41 | -4.2% | $-505.41 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 3564 | 51.3 | 51.7 | $-1633.49 | -4.6% | $-633.49 | -2.8 | done | losing for real |
| always_up | 3564 | 46.9 | 49.6 | $-3460.49 | -9.7% | $-2460.49 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5616 | 48.3 | 49.1 | $-3004.99 |
| ETH | 6132 | 48.3 | 48.5 | $-3709.04 |
| SOL | 6432 | 48.2 | 48.6 | $-3680.94 |
| XRP | 6459 | 48.3 | 48.5 | $-3613.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
