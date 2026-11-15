# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 469 windows, 12861 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1089 | 50.8 | 49.9 | $-272.97 | -2.5% | $727.03 | -0.8 | done | can't tell from luck |
| value_ev10 | 608 | 39.1 | 40.1 | $-352.22 | -5.8% | $647.78 | -1.2 | done | can't tell from luck |
| trend_filter | 745 | 49.7 | 50.7 | $-444.76 | -6.0% | $555.24 | -1.7 | done | can't tell from luck |
| value_ev5 | 899 | 41.0 | 41.8 | $-485.12 | -5.4% | $514.88 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1295 | 49.9 | 50.0 | $-488.91 | -3.8% | $511.09 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1295 | 50.1 | 51.6 | $-928.02 | -7.2% | $71.98 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1089 | 49.2 | 51.8 | $-1010.82 | -9.3% | $-10.82 | -3.2 | done | losing for real |
| coinflip | 1868 | 49.8 | 50.8 | $-1047.11 | -5.6% | $-47.11 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1868 | 49.8 | 51.6 | $-1318.24 | -7.1% | $-318.24 | -3.2 | done | losing for real |
| always_up | 1868 | 46.5 | 50.4 | $-2131.61 | -11.4% | $-1131.61 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2905 | 47.6 | 49.3 | $-2226.85 |
| ETH | 3227 | 48.0 | 48.8 | $-2132.14 |
| SOL | 3349 | 47.8 | 49.3 | $-2557.24 |
| XRP | 3380 | 48.6 | 49.1 | $-1699.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
