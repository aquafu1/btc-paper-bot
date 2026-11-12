# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 130 windows, 3281 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 235 | 62.1 | 53.1 | $+342.92 | +14.6% | $1342.92 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 312 | 56.4 | 52.1 | $+185.15 | +5.9% | $1185.15 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 512 | 52.5 | 50.9 | $-60.57 | -1.2% | $939.43 | -0.3 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 8:30 AM | too few trades (61/200) |
| coinflip | 512 | 51.2 | 51.1 | $-227.26 | -4.4% | $772.74 | -1.0 | done | can't tell from luck |
| value_ev10 | 174 | 36.8 | 40.5 | $-232.46 | -13.4% | $767.54 | -1.5 | Thu 7:00 AM | too few trades (174/200) |
| trend_filter | 169 | 40.8 | 48.9 | $-331.43 | -19.6% | $668.57 | -2.5 | Thu 8:15 AM | too few trades (169/200) |
| value_ev5 | 247 | 36.8 | 42.0 | $-393.07 | -15.9% | $606.93 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 312 | 43.6 | 50.1 | $-491.26 | -15.7% | $508.74 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 235 | 37.9 | 49.1 | $-587.49 | -25.0% | $412.51 | -3.9 | done | losing for real |
| always_up | 512 | 46.1 | 50.2 | $-644.00 | -12.6% | $356.00 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 704 | 45.0 | 49.5 | $-823.11 |
| ETH | 809 | 45.0 | 48.7 | $-919.64 |
| SOL | 870 | 48.6 | 48.7 | $-549.62 |
| XRP | 898 | 50.1 | 49.0 | $-329.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
