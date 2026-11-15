# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 456 windows, 12509 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1063 | 51.4 | 50.0 | $-173.32 | -1.6% | $826.68 | -0.5 | done | can't tell from luck |
| trend_filter | 725 | 50.2 | 50.7 | $-365.66 | -5.0% | $634.34 | -1.4 | done | can't tell from luck |
| value_ev10 | 586 | 38.9 | 40.1 | $-377.06 | -6.4% | $622.94 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1264 | 49.8 | 50.0 | $-493.26 | -3.9% | $506.74 | -1.4 | done | can't tell from luck |
| value_ev5 | 869 | 41.0 | 41.9 | $-501.74 | -5.8% | $498.26 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1264 | 50.2 | 51.6 | $-902.22 | -7.1% | $97.78 | -2.7 | done | losing for real |
| coinflip | 1816 | 49.8 | 50.8 | $-1045.72 | -5.8% | $-45.72 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1063 | 48.6 | 51.7 | $-1089.97 | -10.3% | $-89.97 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1816 | 49.6 | 51.5 | $-1312.21 | -7.2% | $-312.21 | -3.2 | done | losing for real |
| always_up | 1816 | 46.2 | 50.6 | $-2254.38 | -12.4% | $-1254.38 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2828 | 47.5 | 49.3 | $-2298.26 |
| ETH | 3140 | 48.0 | 48.8 | $-2016.23 |
| SOL | 3255 | 47.8 | 49.3 | $-2453.03 |
| XRP | 3286 | 48.5 | 49.2 | $-1900.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
