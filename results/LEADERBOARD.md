# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 1:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1031 windows, 28664 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 531 | 34.7 | 35.1 | $-288.51 | -5.4% | $711.49 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2917 | 51.1 | 50.5 | $-869.38 | -3.0% | $130.62 | -1.6 | done | can't tell from luck |
| value_ev10 | 1318 | 37.6 | 39.2 | $-960.06 | -7.3% | $39.94 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2461 | 49.8 | 49.6 | $-1082.65 | -4.4% | $-82.65 | -2.2 | done | losing for real |
| trend_filter | 1716 | 49.4 | 50.7 | $-1291.06 | -7.5% | $-291.06 | -3.2 | done | losing for real |
| value_ev5 | 1995 | 39.4 | 41.0 | $-1398.88 | -7.0% | $-398.88 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2461 | 50.2 | 51.0 | $-1637.41 | -6.7% | $-637.41 | -3.4 | done | losing for real |
| coinflip | 4116 | 50.5 | 50.3 | $-1681.26 | -4.1% | $-681.26 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2917 | 48.9 | 50.3 | $-1963.27 | -6.7% | $-963.27 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4116 | 50.8 | 51.5 | $-2225.53 | -5.4% | $-1225.53 | -3.6 | done | losing for real |
| always_up | 4116 | 47.4 | 49.5 | $-3591.73 | -8.7% | $-2591.73 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6535 | 48.3 | 49.1 | $-3558.63 |
| ETH | 7114 | 48.2 | 48.5 | $-4353.33 |
| SOL | 7481 | 48.1 | 48.6 | $-4308.57 |
| XRP | 7534 | 48.1 | 48.4 | $-4769.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
