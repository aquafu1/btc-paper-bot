# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 181 windows, 4621 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 450 | 57.8 | 52.4 | $+324.56 | +7.2% | $1324.56 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 340 | 59.7 | 53.1 | $+321.62 | +9.5% | $1321.62 | +1.9 | done | can't tell from luck |
| value_ev20 | 87 | 33.3 | 36.6 | $-143.13 | -16.5% | $856.87 | -1.3 | Sun 4:00 AM | too few trades (87/200) |
| momentum_5m_0.00pct | 716 | 51.5 | 51.3 | $-256.49 | -3.6% | $743.51 | -1.0 | done | can't tell from luck |
| value_ev10 | 233 | 36.5 | 40.6 | $-349.22 | -15.0% | $650.78 | -2.0 | done | losing for real |
| coinflip | 716 | 50.3 | 50.8 | $-397.76 | -5.6% | $602.24 | -1.5 | done | can't tell from luck |
| trend_filter | 230 | 41.3 | 49.3 | $-437.61 | -19.0% | $562.39 | -2.9 | done | losing for real |
| value_ev5 | 343 | 38.2 | 42.4 | $-486.08 | -14.2% | $513.92 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 340 | 40.3 | 49.0 | $-719.57 | -21.2% | $280.43 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 450 | 42.2 | 49.7 | $-813.16 | -18.1% | $186.84 | -3.9 | done | losing for real |
| always_up | 716 | 46.2 | 50.0 | $-857.44 | -12.0% | $142.56 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1008 | 45.7 | 49.4 | $-1034.74 |
| ETH | 1153 | 45.9 | 48.7 | $-1300.35 |
| SOL | 1201 | 47.5 | 49.0 | $-1103.90 |
| XRP | 1259 | 50.0 | 49.1 | $-375.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
