# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 444 windows, 12209 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 226 | 34.5 | 36.0 | $-169.66 | -7.5% | $830.34 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1040 | 51.2 | 50.0 | $-185.76 | -1.8% | $814.24 | -0.6 | done | can't tell from luck |
| trend_filter | 703 | 50.4 | 50.7 | $-335.52 | -4.8% | $664.48 | -1.3 | done | can't tell from luck |
| value_ev10 | 577 | 38.5 | 40.1 | $-435.06 | -7.5% | $564.94 | -1.5 | done | can't tell from luck |
| value_ev5 | 855 | 40.8 | 41.8 | $-530.54 | -6.2% | $469.46 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1232 | 49.6 | 50.0 | $-558.40 | -4.5% | $441.60 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1232 | 50.4 | 51.6 | $-819.66 | -6.7% | $180.34 | -2.4 | done | losing for real |
| coinflip | 1768 | 50.1 | 50.8 | $-918.56 | -5.2% | $81.44 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1040 | 48.8 | 51.7 | $-1043.30 | -10.0% | $-43.30 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1768 | 49.7 | 51.6 | $-1272.88 | -7.2% | $-272.88 | -3.1 | done | losing for real |
| always_up | 1768 | 45.9 | 50.5 | $-2297.89 | -13.0% | $-1297.89 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2761 | 47.5 | 49.3 | $-2204.79 |
| ETH | 3066 | 47.9 | 48.8 | $-2039.45 |
| SOL | 3171 | 47.7 | 49.3 | $-2534.56 |
| XRP | 3211 | 48.6 | 49.2 | $-1788.42 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
