# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 189 windows, 4819 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 352 | 60.2 | 53.1 | $+365.29 | +10.4% | $1365.29 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 468 | 57.5 | 52.5 | $+298.49 | +6.4% | $1298.49 | +1.5 | done | can't tell from luck |
| value_ev20 | 92 | 32.6 | 36.9 | $-168.58 | -18.3% | $831.42 | -1.5 | Sun 7:45 AM | too few trades (92/200) |
| momentum_5m_0.00pct | 748 | 51.9 | 51.3 | $-234.37 | -3.1% | $765.63 | -0.9 | done | can't tell from luck |
| value_ev10 | 243 | 36.6 | 40.7 | $-365.34 | -15.0% | $634.66 | -2.1 | done | losing for real |
| coinflip | 748 | 50.4 | 50.9 | $-410.03 | -5.5% | $589.97 | -1.6 | done | can't tell from luck |
| trend_filter | 242 | 41.3 | 49.4 | $-467.44 | -19.3% | $532.56 | -3.0 | done | losing for real |
| value_ev5 | 358 | 38.5 | 42.5 | $-491.58 | -13.7% | $508.42 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 352 | 39.8 | 49.0 | $-786.81 | -22.4% | $213.19 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 468 | 42.5 | 49.7 | $-833.22 | -17.8% | $166.78 | -3.9 | done | losing for real |
| always_up | 748 | 46.4 | 50.2 | $-901.43 | -12.1% | $98.57 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1055 | 46.1 | 49.5 | $-1061.41 |
| ETH | 1199 | 46.0 | 48.8 | $-1356.51 |
| SOL | 1250 | 47.8 | 49.1 | $-1054.98 |
| XRP | 1315 | 49.7 | 49.1 | $-522.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
