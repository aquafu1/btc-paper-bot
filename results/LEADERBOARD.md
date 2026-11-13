# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 221 windows, 5771 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 569 | 56.1 | 52.8 | $+183.10 | +3.2% | $1183.10 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 453 | 55.2 | 52.6 | $+86.78 | +1.9% | $1086.78 | +0.4 | done | can't tell from luck |
| value_ev20 | 106 | 34.9 | 36.9 | $-105.89 | -10.0% | $894.11 | -0.8 | Sun 8:00 AM | too few trades (106/200) |
| value_ev10 | 282 | 37.6 | 40.9 | $-334.61 | -11.9% | $665.39 | -1.7 | done | can't tell from luck |
| trend_filter | 301 | 44.5 | 50.1 | $-435.99 | -14.5% | $564.01 | -2.5 | done | losing for real |
| value_ev5 | 410 | 39.5 | 42.7 | $-456.42 | -11.1% | $543.58 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 876 | 50.6 | 51.4 | $-483.85 | -5.5% | $516.15 | -1.7 | done | can't tell from luck |
| coinflip | 876 | 50.1 | 51.0 | $-504.35 | -5.8% | $495.65 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 453 | 44.8 | 49.7 | $-613.21 | -13.5% | $386.79 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 569 | 43.9 | 49.6 | $-842.26 | -14.8% | $157.74 | -3.6 | done | losing for real |
| always_up | 876 | 46.5 | 50.3 | $-1025.92 | -11.7% | $-25.92 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1288 | 46.3 | 49.7 | $-1327.72 |
| ETH | 1437 | 46.4 | 49.0 | $-1431.64 |
| SOL | 1491 | 48.1 | 49.4 | $-1172.35 |
| XRP | 1555 | 49.5 | 49.3 | $-600.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
