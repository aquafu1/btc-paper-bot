# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 511 windows, 14090 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1197 | 51.0 | 49.8 | $-207.45 | -1.7% | $792.55 | -0.6 | done | can't tell from luck |
| value_ev10 | 661 | 38.1 | 39.7 | $-493.23 | -7.5% | $506.77 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1429 | 49.7 | 49.7 | $-581.32 | -4.1% | $418.68 | -1.5 | done | can't tell from luck |
| trend_filter | 827 | 49.3 | 50.7 | $-585.13 | -7.1% | $414.87 | -2.1 | done | losing for real |
| value_ev5 | 978 | 40.0 | 41.5 | $-706.61 | -7.2% | $293.39 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1429 | 50.3 | 51.5 | $-934.82 | -6.5% | $65.18 | -2.5 | done | losing for real |
| coinflip | 2036 | 50.0 | 50.7 | $-1065.55 | -5.2% | $-65.55 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1197 | 49.0 | 51.4 | $-1077.12 | -9.0% | $-77.12 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2036 | 49.5 | 51.6 | $-1583.90 | -7.8% | $-583.90 | -3.6 | done | losing for real |
| always_up | 2036 | 46.3 | 50.1 | $-2379.07 | -11.7% | $-1379.07 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3187 | 47.3 | 49.2 | $-2572.63 |
| ETH | 3519 | 48.0 | 48.7 | $-2303.02 |
| SOL | 3673 | 47.6 | 49.0 | $-2742.14 |
| XRP | 3711 | 48.3 | 48.8 | $-2175.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
