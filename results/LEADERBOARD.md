# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 164 windows, 4188 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 307 | 59.6 | 53.1 | $+303.55 | +9.9% | $1303.55 | +1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 405 | 56.8 | 52.6 | $+225.32 | +5.6% | $1225.32 | +1.2 | done | can't tell from luck |
| value_ev20 | 78 | 35.9 | 37.3 | $-81.99 | -10.5% | $918.01 | -0.8 | Sun 5:45 AM | too few trades (78/200) |
| momentum_5m_0.00pct | 648 | 52.0 | 51.1 | $-133.91 | -2.1% | $866.09 | -0.5 | done | can't tell from luck |
| value_ev10 | 213 | 39.0 | 40.9 | $-201.47 | -9.5% | $798.53 | -1.2 | done | can't tell from luck |
| value_ev5 | 313 | 39.9 | 42.6 | $-321.73 | -10.3% | $678.27 | -1.6 | done | can't tell from luck |
| coinflip | 648 | 50.2 | 50.9 | $-370.46 | -5.7% | $629.54 | -1.5 | done | can't tell from luck |
| trend_filter | 216 | 40.7 | 48.9 | $-419.61 | -19.4% | $580.39 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 307 | 40.4 | 49.1 | $-622.13 | -20.3% | $377.87 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 405 | 43.2 | 49.6 | $-633.26 | -15.6% | $366.74 | -3.2 | done | losing for real |
| always_up | 648 | 46.5 | 50.1 | $-739.27 | -11.4% | $260.73 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 908 | 46.3 | 49.5 | $-780.33 |
| ETH | 1045 | 45.8 | 48.9 | $-1108.61 |
| SOL | 1099 | 48.0 | 48.9 | $-836.74 |
| XRP | 1136 | 50.4 | 49.1 | $-269.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
