# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 120 windows, 3052 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 226 | 60.6 | 53.0 | $+272.83 | +12.1% | $1272.83 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 289 | 56.1 | 51.8 | $+174.19 | +6.0% | $1174.19 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 472 | 52.5 | 50.9 | $-45.03 | -1.0% | $954.97 | -0.2 | done | can't tell from luck |
| value_ev10 | 160 | 38.8 | 40.3 | $-138.93 | -8.7% | $861.07 | -0.9 | Thu 7:15 AM | too few trades (160/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 12:15 AM | too few trades (61/200) |
| trend_filter | 159 | 42.1 | 49.0 | $-274.23 | -17.2% | $725.77 | -2.2 | Thu 7:45 AM | too few trades (159/200) |
| coinflip | 472 | 50.2 | 51.0 | $-283.75 | -6.0% | $716.25 | -1.4 | done | can't tell from luck |
| value_ev5 | 226 | 38.1 | 41.9 | $-300.08 | -13.3% | $699.92 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 289 | 43.9 | 50.2 | $-441.09 | -15.3% | $558.91 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 226 | 39.4 | 49.1 | $-497.49 | -22.0% | $502.51 | -3.3 | done | losing for real |
| always_up | 472 | 45.1 | 50.2 | $-666.68 | -14.1% | $333.32 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 655 | 45.5 | 49.6 | $-664.35 |
| ETH | 746 | 45.2 | 48.8 | $-797.51 |
| SOL | 815 | 48.2 | 48.5 | $-593.85 |
| XRP | 836 | 49.8 | 48.8 | $-327.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
