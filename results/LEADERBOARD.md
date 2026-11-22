# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1139 windows, 31463 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 605 | 34.5 | 35.2 | $-385.66 | -6.4% | $614.34 | -1.2 | done | can't tell from luck |
| value_ev10 | 1475 | 38.1 | 39.2 | $-932.14 | -6.3% | $67.86 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3165 | 50.9 | 50.4 | $-997.56 | -3.2% | $2.44 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2656 | 49.7 | 49.4 | $-1128.98 | -4.3% | $-128.98 | -2.2 | done | losing for real |
| value_ev5 | 2231 | 40.0 | 41.1 | $-1325.98 | -5.9% | $-325.98 | -2.4 | done | losing for real |
| trend_filter | 1866 | 49.1 | 50.5 | $-1446.13 | -7.7% | $-446.13 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2656 | 50.3 | 51.1 | $-1686.84 | -6.4% | $-686.84 | -3.4 | done | losing for real |
| coinflip | 4548 | 50.3 | 50.2 | $-1896.85 | -4.2% | $-896.85 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3165 | 49.1 | 50.2 | $-1957.65 | -6.2% | $-957.65 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4548 | 50.3 | 51.4 | $-2794.78 | -6.1% | $-1794.78 | -4.3 | done | losing for real |
| always_up | 4548 | 47.7 | 49.3 | $-3467.40 | -7.6% | $-2467.40 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7209 | 48.3 | 49.0 | $-3724.03 |
| ETH | 7797 | 48.1 | 48.4 | $-4650.81 |
| SOL | 8191 | 48.0 | 48.4 | $-4679.28 |
| XRP | 8266 | 48.1 | 48.3 | $-4965.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
