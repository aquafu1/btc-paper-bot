# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 313 windows, 8370 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 829 | 53.2 | 51.9 | $-143.22 | -1.7% | $856.78 | -0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 683 | 52.7 | 51.8 | $-170.03 | -2.5% | $829.97 | -0.7 | done | can't tell from luck |
| value_ev20 | 155 | 34.2 | 36.6 | $-180.14 | -11.6% | $819.86 | -1.1 | Sun 2:15 AM | too few trades (155/200) |
| value_ev10 | 400 | 38.0 | 40.5 | $-412.57 | -10.3% | $587.43 | -1.8 | done | can't tell from luck |
| value_ev5 | 597 | 39.5 | 42.2 | $-626.70 | -10.5% | $373.30 | -2.3 | done | losing for real |
| trend_filter | 462 | 45.5 | 50.3 | $-648.46 | -14.0% | $351.54 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 683 | 47.3 | 49.9 | $-674.76 | -9.9% | $325.24 | -2.6 | done | losing for real |
| coinflip | 1244 | 50.0 | 50.9 | $-748.45 | -6.0% | $251.55 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 829 | 46.8 | 49.9 | $-847.10 | -10.2% | $152.90 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1244 | 48.6 | 51.3 | $-1160.16 | -9.3% | $-160.16 | -3.4 | done | losing for real |
| always_up | 1244 | 47.3 | 50.5 | $-1298.82 | -10.4% | $-298.82 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1878 | 46.4 | 49.3 | $-1893.26 |
| ETH | 2097 | 46.9 | 48.8 | $-1992.70 |
| SOL | 2179 | 47.9 | 49.4 | $-1785.90 |
| XRP | 2216 | 48.6 | 49.1 | $-1238.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
