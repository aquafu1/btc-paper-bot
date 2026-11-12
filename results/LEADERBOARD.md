# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 124 windows, 3148 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 232 | 61.6 | 53.0 | $+324.87 | +14.0% | $1324.87 | +2.3 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 296 | 56.8 | 51.9 | $+209.78 | +7.1% | $1209.78 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 488 | 52.0 | 50.8 | $-82.27 | -1.7% | $917.73 | -0.4 | done | can't tell from luck |
| value_ev10 | 166 | 38.0 | 40.3 | $-174.30 | -10.5% | $825.70 | -1.2 | Thu 7:15 AM | too few trades (166/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 3:30 AM | too few trades (61/200) |
| coinflip | 488 | 50.4 | 51.0 | $-278.64 | -5.7% | $721.36 | -1.3 | done | can't tell from luck |
| value_ev5 | 235 | 37.9 | 41.9 | $-319.45 | -13.6% | $680.55 | -1.8 | done | can't tell from luck |
| trend_filter | 166 | 41.0 | 48.9 | $-320.28 | -19.3% | $679.72 | -2.5 | Thu 7:15 AM | too few trades (166/200) |
| momentum_15m_0.10pct | 296 | 43.2 | 50.2 | $-492.16 | -16.6% | $507.84 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 232 | 38.4 | 49.2 | $-557.49 | -24.0% | $442.51 | -3.7 | done | losing for real |
| always_up | 488 | 46.3 | 50.3 | $-594.83 | -12.2% | $405.17 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 676 | 45.0 | 49.5 | $-778.75 |
| ETH | 771 | 45.0 | 48.8 | $-861.02 |
| SOL | 837 | 48.5 | 48.6 | $-552.32 |
| XRP | 864 | 50.1 | 48.9 | $-275.34 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
