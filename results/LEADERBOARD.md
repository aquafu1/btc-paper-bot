# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 177 windows, 4525 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 442 | 57.9 | 52.3 | $+340.40 | +7.7% | $1340.40 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 333 | 59.8 | 53.2 | $+318.81 | +9.6% | $1318.81 | +1.9 | done | can't tell from luck |
| value_ev20 | 86 | 33.7 | 36.7 | $-133.13 | -15.5% | $866.87 | -1.2 | Sun 3:00 AM | too few trades (86/200) |
| value_ev10 | 226 | 37.2 | 40.5 | $-302.61 | -13.4% | $697.39 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 700 | 50.9 | 51.2 | $-336.82 | -4.8% | $663.18 | -1.3 | done | can't tell from luck |
| coinflip | 700 | 50.1 | 50.9 | $-409.27 | -5.8% | $590.73 | -1.6 | done | can't tell from luck |
| value_ev5 | 335 | 38.8 | 42.4 | $-429.47 | -12.8% | $570.53 | -2.1 | done | losing for real |
| trend_filter | 228 | 40.8 | 49.2 | $-447.69 | -19.6% | $552.31 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 333 | 40.2 | 48.9 | $-694.80 | -20.9% | $305.20 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 442 | 42.1 | 49.8 | $-820.22 | -18.6% | $179.78 | -4.0 | done | losing for real |
| always_up | 700 | 46.3 | 50.0 | $-826.68 | -11.8% | $173.32 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 984 | 45.7 | 49.4 | $-997.65 |
| ETH | 1127 | 45.6 | 48.8 | $-1331.00 |
| SOL | 1181 | 47.6 | 48.9 | $-1046.26 |
| XRP | 1233 | 50.0 | 49.0 | $-366.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
