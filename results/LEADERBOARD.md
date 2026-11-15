# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 455 windows, 12482 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1059 | 51.2 | 50.0 | $-203.41 | -1.9% | $796.59 | -0.6 | done | can't tell from luck |
| value_ev10 | 586 | 38.9 | 40.1 | $-377.06 | -6.4% | $622.94 | -1.3 | done | can't tell from luck |
| trend_filter | 721 | 49.9 | 50.6 | $-395.75 | -5.5% | $604.25 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1263 | 49.9 | 50.0 | $-483.26 | -3.8% | $516.74 | -1.4 | done | can't tell from luck |
| value_ev5 | 868 | 41.0 | 41.9 | $-491.74 | -5.7% | $508.26 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1263 | 50.1 | 51.6 | $-909.53 | -7.2% | $90.47 | -2.7 | done | losing for real |
| coinflip | 1812 | 49.8 | 50.8 | $-1025.02 | -5.7% | $-25.02 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1059 | 48.8 | 51.8 | $-1049.97 | -9.9% | $-49.97 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1812 | 49.5 | 51.5 | $-1342.30 | -7.4% | $-342.30 | -3.3 | done | losing for real |
| always_up | 1812 | 46.1 | 50.6 | $-2284.47 | -12.6% | $-1284.47 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2819 | 47.4 | 49.3 | $-2294.80 |
| ETH | 3134 | 48.0 | 48.8 | $-2024.29 |
| SOL | 3249 | 47.7 | 49.3 | $-2489.53 |
| XRP | 3280 | 48.4 | 49.2 | $-1906.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
