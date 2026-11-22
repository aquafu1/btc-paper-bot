# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1096 windows, 30330 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 575 | 34.4 | 35.0 | $-350.36 | -6.1% | $649.64 | -1.1 | done | can't tell from luck |
| value_ev10 | 1408 | 38.1 | 39.1 | $-853.68 | -6.1% | $146.32 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3063 | 51.0 | 50.5 | $-936.01 | -3.1% | $63.99 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2578 | 49.7 | 49.4 | $-1120.11 | -4.3% | $-120.11 | -2.2 | done | losing for real |
| value_ev5 | 2138 | 40.0 | 41.0 | $-1213.29 | -5.7% | $-213.29 | -2.2 | done | losing for real |
| trend_filter | 1799 | 49.4 | 50.5 | $-1317.14 | -7.3% | $-317.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2578 | 50.3 | 51.1 | $-1632.59 | -6.3% | $-632.59 | -3.3 | done | losing for real |
| coinflip | 4376 | 50.5 | 50.2 | $-1650.62 | -3.8% | $-650.62 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 3063 | 49.0 | 50.2 | $-1960.38 | -6.4% | $-960.38 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4376 | 50.8 | 51.4 | $-2207.91 | -5.0% | $-1207.91 | -3.4 | done | losing for real |
| always_up | 4376 | 47.5 | 49.3 | $-3521.00 | -8.0% | $-2521.00 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6936 | 48.4 | 49.0 | $-3381.41 |
| ETH | 7516 | 48.2 | 48.4 | $-4437.01 |
| SOL | 7900 | 48.1 | 48.4 | $-4407.47 |
| XRP | 7978 | 48.3 | 48.2 | $-4537.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
