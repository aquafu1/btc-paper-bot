# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 556 windows, 15417 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1312 | 51.1 | 49.6 | $-278.15 | -2.1% | $721.85 | -0.8 | done | can't tell from luck |
| value_ev20 | 305 | 33.1 | 35.2 | $-345.92 | -11.3% | $654.08 | -1.5 | done | can't tell from luck |
| trend_filter | 894 | 50.3 | 51.0 | $-519.63 | -5.8% | $480.37 | -1.8 | done | can't tell from luck |
| value_ev10 | 730 | 37.1 | 39.3 | $-742.65 | -10.2% | $257.35 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1565 | 49.4 | 49.8 | $-824.70 | -5.3% | $175.30 | -2.1 | done | losing for real |
| value_ev5 | 1086 | 39.6 | 41.2 | $-887.77 | -8.2% | $112.23 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1565 | 50.6 | 51.1 | $-916.85 | -5.9% | $83.15 | -2.4 | done | losing for real |
| coinflip | 2216 | 49.9 | 50.5 | $-1267.48 | -5.7% | $-267.48 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1312 | 48.9 | 51.2 | $-1270.63 | -9.7% | $-270.63 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2216 | 50.3 | 51.8 | $-1553.19 | -7.0% | $-553.19 | -3.4 | done | losing for real |
| always_up | 2216 | 46.7 | 49.9 | $-2423.66 | -10.9% | $-1423.66 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3486 | 47.5 | 49.2 | $-2823.93 |
| ETH | 3841 | 47.8 | 48.6 | $-2807.24 |
| SOL | 4023 | 47.7 | 48.7 | $-3102.32 |
| XRP | 4067 | 48.5 | 48.6 | $-2297.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
